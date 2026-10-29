import json
from pathlib import Path
import asyncio
import subprocess

class ColumnNormalizer:
    def _get_data_type(self, value):
        if isinstance(value, bool):
            return "boolean"
        if isinstance(value, (int, float)):
            return "number"
        if isinstance(value, str):
            return "string"
        return "unknown"

    def _get_unique_columns(self, response, key_field):
        if isinstance(response[key_field], list):
            return [
                {
                    "key": key,
                    "label": key.title(),
                    "type": self._get_data_type(value)
                }
                for key, value in response[key_field][0].items()
            ]
        return [
            {
                "key": key,
                "label": key.title(),
                "type": self._get_data_type(value)
            }
            for key, value in response.get(key_field, {}).items()
        ]

    def collect_column_name(self, response, key_field):
        unique_columns = self._get_unique_columns(response, key_field)
        response.update({f"{key_field}_columns": unique_columns})

class ProcessRequest:
 
    async def _run_markdown_conversion(self, input_file, output_file):
        command = ["pandoc", "-f", "markdown-yaml_metadata_block", input_file, "-o", output_file]
        await self.run_query(command)

    async def run_query(self, command):
        try:
            result = await asyncio.to_thread(
                subprocess.run,
                command,
                capture_output=True,
                text=True
            )
            return result.stdout
        except:
            return " ".join(command)

    async def render_json(self, command):
        normalizer = ColumnNormalizer()
        await self.run_query(command)
        with open(Path.cwd() / "report.json", "r") as f:
            response = json.load(f)
            normalizer.collect_column_name(response, "summary")
            normalizer.collect_column_name(response, "results")
            if "query_performance" in response.keys() and len(response["query_performance"]) > 0:
                normalizer.collect_column_name(response, "query_performance")
            if "failures" in response.keys() and len(response["failures"]) > 0:
                normalizer.collect_column_name(response, "failures")
            return response

    async def render_github(self, command):
        filename = "github-report"
        input_file = str(Path.cwd() / f"{filename}.md")
        output_file = str(Path.cwd() / f"{filename}.html")
        await self.run_query(command)
        await self._run_markdown_conversion(input_file, output_file)
        with open(output_file, "r") as f:
            html = f.read()
        return html

    async def render_html(self, command):
        await self.run_query(command)
        with open(Path.cwd() / "index.html", "r") as f:
            html = f.read()
        return html

    async def render_markdown(self, command):
        filename = "report"
        input_file = str(Path.cwd() / f"{filename}.md")
        output_file = str(Path.cwd() / f"{filename}.html")
        await self.run_query(command)
        await self._run_markdown_conversion(input_file, output_file)
        with open(output_file, "r") as f:
            html = f.read()
        return html

    async def render_pdf(self, command):
        filename = "report"
        input_file = str(Path.cwd() / f"{filename}.pdf")
        output_file = str(Path.cwd() / f"{filename}.html")
        await self.run_query(command)
        command = ["pdftohtml", input_file, output_file]
        await self.run_query(command)
        with open(output_file, "r") as f:
            html = f.read()
        return html