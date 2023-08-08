from enum import Enum

from PyQt5.QtCore import QLocale

from qfluentwidgets import (qconfig, QConfig, ConfigItem, FolderValidator, BoolValidator,
                            OptionsConfigItem, OptionsValidator, ConfigSerializer, RangeConfigItem, RangeValidator)


class Language(Enum):
    CHINESE_SIMPLIFIED = QLocale(QLocale.Chinese, QLocale.China)
    ENGLISH = QLocale(QLocale.English)
    AUTO = QLocale()


class LanguageSerializer(ConfigSerializer):

    def serialize(self, language: Language):
        return language.value.name() if language != Language.AUTO else "Auto"

    def deserialize(self, value: str):
        return Language(QLocale(value)) if value != 'Auto' else Language.AUTO


class Config(QConfig):
    lolFolder = ConfigItem("General", "LolPath", "", FolderValidator())
    enableStartWithComputer = ConfigItem("General", "EnableStartWithComputer",
                                         False, BoolValidator())
    enableStartLolWithApp = ConfigItem("General", "EnableStartLolWithApp",
                                       False, BoolValidator())

    dpiScale = OptionsConfigItem("Personalization",
                                 "DpiScale",
                                 "Auto",
                                 OptionsValidator(
                                     [1, 1.25, 1.5, 1.75, 2, "Auto"]),
                                 restart=True)

    language = OptionsConfigItem("Personalization",
                                 "Language",
                                 Language.AUTO,
                                 OptionsValidator(Language),
                                 LanguageSerializer(),
                                 restart=True)

    careerGamesNumber = RangeConfigItem("Functions", "CareerGamesNumber", 20,
                                        RangeValidator(1, 999))

    showTierInGameInfo = ConfigItem("Functions", "ShowTierInGameInfo", False,
                                    BoolValidator())
    enableAutoAcceptMatching = ConfigItem("Functions",
                                          "EnableAutoAcceptMatching", False,
                                          BoolValidator())


YEAR = 2023
AUTHOR = "Zaphkiel"
VERSION = "0.2.3"
FEEDBACK_URL = "https://github.com/Zzaphkiel/Seraphine/issues"
GITHUB_URL = "https://github.com/Zzaphkiel/Seraphine"

cfg = Config()
qconfig.load('app/config/config.json', cfg)
