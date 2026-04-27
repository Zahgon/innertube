from dataclasses import dataclass
from enum import Enum
from typing import Optional, Union

__all__ = ("Location", "Language", "Locale")


class Location(Enum):
    """ISO 3166-1 alpha-2 Country Code"""

    country_code: str
    country_name: str

    def __init__(self, code: str, name: str) -> None:
        self.country_code = code
        self.country_name = name

    def __str__(self) -> str:
        return self.country_code

    @classmethod
    def from_code(cls, country_code: str, /) -> Optional["Location"]:
        pass

    ALGERIA = ("DZ", "Algeria")
    ARGENTINA = ("AR", "Argentina")
    AUSTRALIA = ("AU", "Australia")
    AUSTRIA = ("AT", "Austria")
    AZERBAIJAN = ("AZ", "Azerbaijan")
    BAHRAIN = ("BH", "Bahrain")
    BANGLADESH = ("BD", "Bangladesh")
    BELARUS = ("BY", "Belarus")
    BELGIUM = ("BE", "Belgium")
    BOLIVIA = ("BO", "Bolivia")
    BOSNIA_AND_HERZEGOVINA = ("BA", "Bosnia and Herzegovina")
    BRAZIL = ("BR", "Brazil")
    BULGARIA = ("BG", "Bulgaria")
    CAMBODIA = ("KH", "Cambodia")
    CANADA = ("CA", "Canada")
    CHILE = ("CL", "Chile")
    COLOMBIA = ("CO", "Colombia")
    COSTA_RICA = ("CR", "Costa Rica")
    CROATIA = ("HR", "Croatia")
    CYPRUS = ("CY", "Cyprus")
    CZECHIA = ("CZ", "Czechia")
    DENMARK = ("DK", "Denmark")
    DOMINICAN_REPUBLIC = ("DO", "Dominican Republic")
    ECUADOR = ("EC", "Ecuador")
    EGYPT = ("EG", "Egypt")
    EL_SALVADOR = ("SV", "El Salvador")
    ESTONIA = ("EE", "Estonia")
    FINLAND = ("FI", "Finland")
    FRANCE = ("FR", "France")
    GEORGIA = ("GE", "Georgia")
    GERMANY = ("DE", "Germany")
    GHANA = ("GH", "Ghana")
    GREECE = ("GR", "Greece")
    GUATEMALA = ("GT", "Guatemala")
    HONDURAS = ("HN", "Honduras")
    HONG_KONG = ("HK", "Hong Kong")
    HUNGARY = ("HU", "Hungary")
    ICELAND = ("IS", "Iceland")
    INDIA = ("IN", "India")
    INDONESIA = ("ID", "Indonesia")
    IRAQ = ("IQ", "Iraq")
    IRELAND = ("IE", "Ireland")
    ISRAEL = ("IL", "Israel")
    ITALY = ("IT", "Italy")
    JAMAICA = ("JM", "Jamaica")
    JAPAN = ("JP", "Japan")
    JORDAN = ("JO", "Jordan")
    KAZAKHSTAN = ("KZ", "Kazakhstan")
    KENYA = ("KE", "Kenya")
    KUWAIT = ("KW", "Kuwait")
    LAOS = ("LA", "Laos")
    LATVIA = ("LV", "Latvia")
    LEBANON = ("LB", "Lebanon")
    LIBYA = ("LY", "Libya")
    LIECHTENSTEIN = ("LI", "Liechtenstein")
    LITHUANIA = ("LT", "Lithuania")
    LUXEMBOURG = ("LU", "Luxembourg")
    MALAYSIA = ("MY", "Malaysia")
    MALTA = ("MT", "Malta")
    MEXICO = ("MX", "Mexico")
    MOLDOVA = ("MD", "Moldova")
    MONTENEGRO = ("ME", "Montenegro")
    MOROCCO = ("MA", "Morocco")
    NEPAL = ("NP", "Nepal")
    NETHERLANDS = ("NL", "Netherlands")
    NEW_ZEALAND = ("NZ", "New Zealand")
    NICARAGUA = ("NI", "Nicaragua")
    NIGERIA = ("NG", "Nigeria")
    NORTH_MACEDONIA = ("MK", "North Macedonia")
    NORWAY = ("NO", "Norway")
    OMAN = ("OM", "Oman")
    PAKISTAN = ("PK", "Pakistan")
    PANAMA = ("PA", "Panama")
    PAPUA_NEW_GUINEA = ("PG", "Papua New Guinea")
    PARAGUAY = ("PY", "Paraguay")
    PERU = ("PE", "Peru")
    PHILIPPINES = ("PH", "Philippines")
    POLAND = ("PL", "Poland")
    PORTUGAL = ("PT", "Portugal")
    PUERTO_RICO = ("PR", "Puerto Rico")
    QATAR = ("QA", "Qatar")
    ROMANIA = ("RO", "Romania")
    RUSSIA = ("RU", "Russia")
    SAUDI_ARABIA = ("SA", "Saudi Arabia")
    SENEGAL = ("SN", "Senegal")
    SERBIA = ("RS", "Serbia")
    SINGAPORE = ("SG", "Singapore")
    SLOVAKIA = ("SK", "Slovakia")
    SLOVENIA = ("SI", "Slovenia")
    SOUTH_AFRICA = ("ZA", "South Africa")
    SOUTH_KOREA = ("KR", "South Korea")
    SPAIN = ("ES", "Spain")
    SRI_LANKA = ("LK", "Sri Lanka")
    SWEDEN = ("SE", "Sweden")
    SWITZERLAND = ("CH", "Switzerland")
    TAIWAN = ("TW", "Taiwan")
    TANZANIA = ("TZ", "Tanzania")
    THAILAND = ("TH", "Thailand")
    TUNISIA = ("TN", "Tunisia")
    TURKEY = ("TR", "Turkey")
    UGANDA = ("UG", "Uganda")
    UKRAINE = ("UA", "Ukraine")
    UNITED_ARAB_EMIRATES = ("AE", "United Arab Emirates")
    UNITED_KINGDOM = ("GB", "United Kingdom")
    UNITED_STATES = ("US", "United States")
    URUGUAY = ("UY", "Uruguay")
    VENEZUELA = ("VE", "Venezuela")
    VIETNAM = ("VN", "Vietnam")
    YEMEN = ("YE", "Yemen")
    ZIMBABWE = ("ZW", "Zimbabwe")


class Language(Enum):
    """IETF BCP-47 Language"""

    language_code: str
    language_name: str
    language_name_native: str

    def __init__(
        self, language_code: str, language_name: str, language_name_native: str
    ) -> None:
        self.language_code = language_code
        self.language_name = language_name
        self.language_name_native = language_name_native

    def __str__(self) -> str:
        return self.language_code

    @classmethod
    def from_code(cls, language_code: str, /) -> Optional["Language"]:
        pass

    AFRIKAANS = ("af", "Afrikaans", "Afrikaans")
    AZERBAIJANI = ("az", "Azerbaijani", "AzÉ™rbaycan")
    INDONESIAN = ("id", "Indonesian", "Bahasa Indonesia")
    MALAY = ("ms", "Malay", "Bahasa Malaysia")
    BOSNIAN = ("bs", "Bosnian", "Bosanski")
    CATALAN = ("ca", "Catalan", "CatalÃ ")
    CZECH = ("cs", "Czech", "ÄŒeÅ¡tina")
    DANISH = ("da", "Danish", "Dansk")
    GERMAN = ("de", "German", "Deutsch")
    ESTONIAN = ("et", "Estonian", "Eesti")
    ENGLISH_INDIA = ("en-IN", "English (India)", "English (India)")
    ENGLISH_UK = ("en-GB", "English (UK)", "English (UK)")
    ENGLISH_US = ("en-US", "English (US)", "English (US)")
    SPANISH_SPAIN = ("es", "Spanish (Spain)", "EspaÃ±ol (EspaÃ±a)")
    SPANISH_LATIN_AMERICA = (
        "es-419",
        "Spanish (Latin America)",
        "EspaÃ±ol (LatinoamÃ©rica)",
    )
    SPANISH_US = ("es-US", "Spanish (US)", "EspaÃ±ol (US)")
    BASQUE = ("eu", "Basque", "Euskara")
    FILIPINO = ("fil", "Filipino", "Filipino")
    FRENCH = ("fr", "French", "FranÃ§ais")
    FRENCH_CANADA = ("fr-CA", "French (Canada)", "FranÃ§ais (Canada)")
    GALICIAN = ("gl", "Galician", "Galego")
    CROATIAN = ("hr", "Croatian", "Hrvatski")
    ZULU = ("zu", "Zulu", "IsiZulu")
    ICELANDIC = ("is", "Icelandic", "Ã�slenska")
    ITALIAN = ("it", "Italian", "Italiano")
    KISWAHILI = ("sw", "Kiswahili", "Kiswahili")
    LATVIAN = ("lv", "Latvian", "LatvieÅ¡u valoda")
    LITHUANIAN = ("lt", "Lithuanian", "LietuviÅ³")
    HUNGARIAN = ("hu", "Hungarian", "Magyar")
    DUTCH = ("nl", "Dutch", "Nederlands")
    NORWEGIAN = ("no", "Norwegian", "Norsk")
    UZBEK = ("uz", "Uzbek", "Oâ€˜zbek")
    POLISH = ("pl", "Polish", "Polski")
    PORTUGUESE = ("pt-PT", "Portuguese", "PortuguÃªs")
    PORTUGUESE_BRASIL = ("pt", "Portuguese (Brasil)", "PortuguÃªs (Brasil)")
    ROMANIAN = ("ro", "Romanian", "RomÃ¢nÄƒ")
    ALBANIAN = ("sq", "Albanian", "Shqip")
    SLOVAK = ("sk", "Slovak", "SlovenÄ�ina")
    SLOVENIAN = ("sl", "Slovenian", "SlovenÅ¡Ä�ina")
    SERBIAN = ("sr-Latn", "Serbian", "Srpski")
    FINNISH = ("fi", "Finnish", "Suomi")
    SWEDISH = ("sv", "Swedish", "Svenska")
    VIETNAMESE = ("vi", "Vietnamese", "Tiáº¿ng Viá»‡t")
    TURKISH = ("tr", "Turkish", "TÃ¼rkÃ§e")
    BELARUSIAN = ("be", "Belarusian", "Ð‘ÐµÐ»Ð°Ñ€ÑƒÑ�ÐºÐ°Ñ�")
    BULGARIAN = ("bg", "Bulgarian", "Ð‘ÑŠÐ»Ð³Ð°Ñ€Ñ�ÐºÐ¸")
    KYRGYZ = ("ky", "Kyrgyz", "ÐšÑ‹Ñ€Ð³Ñ‹Ð·Ñ‡Ð°")
    KAZAKH = ("kk", "Kazakh", "ÒšÐ°Ð·Ð°Ò› Ð¢Ñ–Ð»Ñ–")
    MACEDONIAN = ("mk", "Macedonian", "ÐœÐ°ÐºÐµÐ´Ð¾Ð½Ñ�ÐºÐ¸")
    MONGOLIAN = ("mn", "Mongolian", "ÐœÐ¾Ð½Ð³Ð¾Ð»")
    RUSSIAN = ("ru", "Russian", "Ð ÑƒÑ�Ñ�ÐºÐ¸Ð¹")
    SERBIAN_CYRILLIC = ("sr", "Serbian (Cyrillic)", "Ð¡Ñ€Ð¿Ñ�ÐºÐ¸")
    UKRAINIAN = ("uk", "Ukrainian", "Ð£ÐºÑ€Ð°Ñ—Ð½Ñ�ÑŒÐºÐ°")
    GREEK = ("el", "Greek", "Î•Î»Î»Î·Î½Î¹ÎºÎ¬")
    ARMENIAN = ("hy", "Armenian", "Õ€Õ¡ÕµÕ¥Ö€Õ¥Õ¶")
    HEBREW = ("he", "Hebrew", "×¢×‘×¨×™×ª")
    URDU = ("ur", "Urdu", "Ø§Ø±Ø¯Ùˆ")
    ARABIC = ("ar", "Arabic", "Ø§Ù„Ø¹Ø±Ø¨ÙŠØ©")
    PERSIAN = ("fa", "Persian", "Ù�Ø§Ø±Ø³ÛŒ")
    NEPALI = ("ne", "Nepali", "à¤¨à¥‡à¤ªà¤¾à¤²à¥€")
    MARATHI = ("mr", "Marathi", "à¤®à¤°à¤¾à¤ à¥€")
    HINDI = ("hi", "Hindi", "à¤¹à¤¿à¤¨à¥�à¤¦à¥€")
    ASSAMESE = ("as", "Assamese", "à¦…à¦¸à¦®à§€à¦¯à¦¼à¦¾")
    BENGALI = ("bn", "Bengali", "à¦¬à¦¾à¦‚à¦²à¦¾")
    PUNJABI = ("pa", "Punjabi", "à¨ªà©°à¨œà¨¾à¨¬à©€")
    GUJARATI = ("gu", "Gujarati", "àª—à«�àªœàª°àª¾àª¤à«€")
    ODIA = ("or", "Odia", "à¬“à¬¡à¬¼à¬¿à¬†")
    TAMIL = ("ta", "Tamil", "à®¤à®®à®¿à®´à¯�")
    TELUGU = ("te", "Telugu", "à°¤à±†à°²à±�à°—à±�")
    KANNADA = ("kn", "Kannada", "à²•à²¨à³�à²¨à²¡")
    MALAYALAM = ("ml", "Malayalam", "à´®à´²à´¯à´¾à´³à´‚")
    SINHALA = ("si", "Sinhala", "à·ƒà·’à¶‚à·„à¶½")
    THAI = ("th", "Thai", "à¸ à¸²à¸©à¸²à¹„à¸—à¸¢")
    LAO = ("lo", "Lao", "àº¥àº²àº§")
    BURMESE = ("my", "Burmese", "á€—á€™á€¬")
    GEORGIAN = ("ka", "Georgian", "áƒ¥áƒ�áƒ áƒ—áƒ£áƒšáƒ˜")
    AMHARIC = ("am", "Amharic", "áŠ áˆ›áˆ­áŠ›")
    KHMER = ("km", "Khmer", "áž�áŸ’áž˜áŸ‚ážš")
    CHINESE_SIMPLIFIED = ("zh-CN", "Chinese (Simplified)", "ä¸­æ–‡ (ç®€ä½“)")
    CHINESE_TRADITIONAL = ("zh-TW", "Chinese (Traditional)", "ä¸­æ–‡ (ç¹�é«”)")
    CHINESE_HONG_KONG = ("zh-HK", "Chinese (Hong Kong)", "ä¸­æ–‡ (é¦™æ¸¯)")
    JAPANESE = ("ja", "Japanese", "æ—¥æœ¬èªž")
    KOREAN = ("ko", "Korean", "í•œêµ­ì–´")


@dataclass
class Locale:
    language: str  # HL (Host Language)
    location: Optional[str] = None  # GL (Geographic Location)

    def __init__(
        self, language: Union[str, Language], location: Optional[Union[str, Location]]
    ) -> None:
        if isinstance(language, Language):
            language = language.language_code
        if isinstance(location, Location):
            location = location.country_code

        self.language = language
        self.location = location

    def accept_language(self) -> str:
        pass
