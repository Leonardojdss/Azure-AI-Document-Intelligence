from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from dotenv import load_dotenv
import os

load_dotenv()

endpoint = os.getenv("DOC_INT_ENDPOINT")
key = os.getenv("DOC_INT_API_KEY")
model_id = os.getenv("MODEL_ID")

def extract_document(path: str):

    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key))

    with open(path, "rb") as doc_input:
        response = document_analysis_client.begin_analyze_document(
            model_id,
            document=doc_input
        )

    result = response.result()

    for idx, document in enumerate(result.documents):
        print("--------Analyzing document #{}--------".format(idx + 1))
        print("Document has type {}".format(document.doc_type))
        print("Document has confidence {}".format(document.confidence))
        print("Document was analyzed by model with ID {}".format(result.model_id))
        for name, field in document.fields.items():
            field_value = field.value if field.value else field.content
            print("Found field '{}' with value '{}' and with confidence {}".format(name, field_value, field.confidence))

    print("-----------------------------------")

if __name__ == "__main__":
    path_document = "examples_docs/validation/test1.jpg"
    extraction = extract_document(path_document)
