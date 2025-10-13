import os
import allure
from datetime import datetime
from typing import Optional

class AllureHelper:
    """
    Classe utilitária para integração com Allure Reports
    Fornece métodos para capturar screenshots e anexar ao relatório
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.screenshots_dir = "screenshots"
        self._ensure_screenshots_dir()
    
    def _ensure_screenshots_dir(self):
        """Cria o diretório de screenshots se não existir"""
        if not os.path.exists(self.screenshots_dir):
            os.makedirs(self.screenshots_dir)
    
    def take_screenshot(self, step_name: str, description: Optional[str] = None) -> str:
        """
        Captura screenshot e anexa ao relatório Allure
        
        Args:
            step_name: Nome do passo/ação sendo executada
            description: Descrição opcional do screenshot
            
        Returns:
            str: Caminho do arquivo de screenshot salvo
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
        filename = f"{step_name}_{timestamp}.png"
        filepath = os.path.join(self.screenshots_dir, filename)
        
        try:
            # Captura screenshot
            screenshot_data = self.driver.get_screenshot_as_png()
            
            # Salva arquivo local
            with open(filepath, 'wb') as f:
                f.write(screenshot_data)
            
            # Anexa ao relatório Allure
            attachment_name = description or f"Screenshot - {step_name}"
            allure.attach(
                screenshot_data,
                name=attachment_name,
                attachment_type=allure.attachment_type.PNG
            )
            
            print(f"📸 Screenshot capturado: {filename}")
            return filepath
            
        except Exception as e:
            print(f"❌ Erro ao capturar screenshot: {str(e)}")
            return ""
    
    def attach_text(self, content: str, name: str, attachment_type=allure.attachment_type.TEXT):
        """
        Anexa texto ao relatório Allure
        
        Args:
            content: Conteúdo do texto
            name: Nome do anexo
            attachment_type: Tipo do anexo (padrão: TEXT)
        """
        allure.attach(content, name=name, attachment_type=attachment_type)
    
    def step(self, step_name: str, take_screenshot: bool = True):
        """
        Decorator para marcar passos do teste com screenshot automático
        
        Args:
            step_name: Nome do passo
            take_screenshot: Se deve capturar screenshot automaticamente
        """
        def decorator(func):
            def wrapper(*args, **kwargs):
                with allure.step(step_name):
                    if take_screenshot and hasattr(self, 'driver'):
                        self.take_screenshot(
                            step_name.lower().replace(' ', '_'),
                            f"Antes de: {step_name}"
                        )
                    
                    result = func(*args, **kwargs)
                    
                    if take_screenshot and hasattr(self, 'driver'):
                        self.take_screenshot(
                            f"{step_name.lower().replace(' ', '_')}_after",
                            f"Depois de: {step_name}"
                        )
                    
                    return result
            return wrapper
        return decorator

def allure_step_with_screenshot(driver, step_name: str, description: Optional[str] = None):
    """
    Context manager para passos com screenshot automático
    
    Usage:
        with allure_step_with_screenshot(driver, "Login do usuário"):
            login_page.login(username, password)
    """
    class StepContext:
        def __enter__(self):
            allure.step(step_name).__enter__()
            helper = AllureHelper(driver)
            helper.take_screenshot(
                step_name.lower().replace(' ', '_') + "_before",
                f"Antes de: {step_name}"
            )
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            helper = AllureHelper(driver)
            if exc_type is None:
                helper.take_screenshot(
                    step_name.lower().replace(' ', '_') + "_after",
                    f"Depois de: {step_name}"
                )
            else:
                helper.take_screenshot(
                    step_name.lower().replace(' ', '_') + "_error",
                    f"Erro em: {step_name}"
                )
            allure.step(step_name).__exit__(exc_type, exc_val, exc_tb)
    
    return StepContext()