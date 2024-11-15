from .proxy import Proxy
from src.analyze import *
from src.data.prog.support.doc_extensions import Supported_Document_Extensions
from pathlib import Path

class Analyzer_Proxy(Proxy):
    def _get_instance_except(self, instance, err):
        instance = analyzer.Analyzer('')
        return super()._get_instance_except(self, instance, err)

    def get_instance(read_file: str):
        support = Supported_Document_Extensions()
        extension = Path(read_file).suffix
        if extension in support.doc_files:
            return docx_analyzer.Docx_Analyzer(read_file)
        elif extension in support.fdx_files:
            raise TypeError('class \'Fdx_Analyzer\' is still being developed! Update to latest version or wait for a working release!')
            return fdx_analyzer.Fdx_Analyzer(read_file)
        elif extension in support.md_files:
            raise TypeError('class \'Markdown_Analyzer\' is still being developed! Update to latest version or wait for a working release!')
            return md_analyzer.Markdown_analyzer(read_file)
        elif extension in support.raw_files:
            return raw_analyzer.Raw_Analyzer(read_file)
        else:
            Analyzer_Proxy._get_instance_except('TypeError: Extension in document \"{0}\" is not supported in Text2RenPy'.format(read_file))