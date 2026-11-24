import unittest
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from correlacionar import correlacionar
class TestSIEM(unittest.TestCase):
    def test_alerta(self):
        self.assertEqual(len(correlacionar(json.loads(Path("eventos.json").read_text()))),1)
    def test_janela(self):
        self.assertEqual(correlacionar([{"segundo":i*61,"ip":"192.0.2.1","evento":"ssh_failure"} for i in range(5)]),[])
    def test_origens(self):
        self.assertEqual(correlacionar([{"segundo":i,"ip":str(i),"evento":"ssh_failure"} for i in range(5)]),[])
    def test_xml(self):
        r=ET.parse("local_rules.xml").getroot().find("rule")
        self.assertEqual(r.attrib["id"],"100110")
        self.assertEqual(r.attrib["frequency"],"5")
