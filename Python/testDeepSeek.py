from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core import ServiceContext
from llama_index.llms import Ollama


# Создаем объект LLM для взаимодействия с DeepSeek
llm = Ollama(model="deepseek-r1:1.5b")

# Создаем контекст сервиса
service_context = ServiceContext.from_defaults(llm=llm)

# Путь к папке со структурой индекса
storage_context = StorageContext.from_defaults(persist_dir="./storage")

# Загружаем индекс из хранилища
index = load_index_from_storage(storage_context)

# Выполняем запрос
query = "Объясни, как работает декоратор в Python."
response = index.query(query)
print(response)
