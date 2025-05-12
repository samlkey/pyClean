class ExtensionLibrary:
    def __init__(self):
        # Extensions
        self.extensions = {
            "Documents": [
                ".txt",    # Plain text
                ".doc",    # Microsoft Word (pre-2007)
                ".docx",   # Microsoft Word (Open XML)
                ".rtf",    # Rich Text Format
                ".odt",    # OpenDocument Text
                ".pdf",    # Portable Document Format
                ".xls",    # Microsoft Excel (pre-2007)
                ".xlsx",   # Microsoft Excel (Open XML)
                ".ods",    # OpenDocument Spreadsheet
                ".ppt",    # Microsoft PowerPoint (pre-2007)
                ".pptx",   # Microsoft PowerPoint (Open XML)
                ".odp",    # OpenDocument Presentation
                ".md",     # Markdown
                ".html",   # HTML
                ".htm",    # HTML
                ".xml",    # XML
                ".csv"     # CSV
            ],
            "Pictures/Images": [
                ".jpg", ".jpeg", ".png", ".gif", ".bmp",
                ".tiff", ".tif", ".webp", ".heic", ".heif",
                ".svg", ".raw", ".cr2", ".nef", ".orf", ".sr2"
            ],
            "Audio/Video": [
                ".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv", ".webm", ".mpeg", ".mpg", ".3gp",
                ".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a", ".alac", ".aiff", ".opus"
            ]
        }