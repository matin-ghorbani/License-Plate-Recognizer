from io import TextIOWrapper
from lxml import etree as et
from lxml.etree import _Element

IMAGES_DATASET: str
GT_PATH: str

words_dict: dict[str, str]

def prepare_dataset(images_dataset_path: str, dataset_type: str)-> None:
    gt_file: TextIOWrapper
    parser = et.XMLParser
    root: _Element
    
    file: str
    path: str
    xml_name: str

    persian_word: str
    latin_word = list[str]
    
