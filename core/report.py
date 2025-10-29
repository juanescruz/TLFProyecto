# core/report.py
import pandas as pd
from datetime import datetime

class ReportGenerator:
    """Genera y exporta reportes de validación."""

    def export_csv(self, df: pd.DataFrame, filename: str = None):
        filename = filename or f"reporte_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(filename, index=False, encoding="utf-8")
        return filename

    def export_json(self, df: pd.DataFrame, filename: str = None):
        filename = filename or f"reporte_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        df.to_json(filename, orient="records", indent=2, force_ascii=False)
        return filename
