from nonebot.plugin import get_plugin_config
from pydantic import BaseModel, Field
import os


class ScopedConfig(BaseModel):
    language: str = Field(default="zh-cn")
    """插件渲染图片所使用的语言"""
    type: int = Field(default=0)
    """插件发送的消息类型"""
    host: str = Field(default=os.getenv("MCC__HOST", os.getenv("MCC_HOST", "")))
    """插件查询的MC服务器地址"""


class Config(BaseModel):
    mcc: ScopedConfig = Field(default_factory=ScopedConfig)
    """MCCheck Config"""


config: ScopedConfig = get_plugin_config(Config).mcc
