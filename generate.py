import json
import yaml
import sys


def _loadYaml(yamlfile):
    with open(yamlfile, 'r', encoding='utf8') as linksYmlData:
        linksList = yaml.load(linksYmlData, Loader=yaml.FullLoader)
    return linksList


def _renderJson(yamlList, jsonFile):
    with open(jsonFile, 'w', encoding='utf8') as linksJsonData:
        linksJsonData.write(json.dumps(yamlList, ensure_ascii=False))
        linksJsonData.close()

yamlOrigin = "./src/links.yml"
jsonTarget = "./links/links.json"
_renderJson(_loadYaml(yamlOrigin), jsonTarget)
