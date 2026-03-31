## CourseMind — интелигентен асистент за университетски курсове (Weaviate Agents)

Приложение, което използва **Weaviate Query Agent** за отговаряне на въпроси на естествен език върху данни, съхранени в **Weaviate Cloud**. Домейнът е **университетски курсове**.

### Колекции (Weaviate)

- **`Courses`**: курсове с полета като `title`, `description`, `language`, `ects`, `semester`, `level`, `tags`, `department`, `instructorId`
- **`Instructors`**: преподаватели с полета като `fullName`, `bio`, `department`, `researchInterests`, `email`

`Courses` съдържа богати **текстови полета** (`title`, `description`) подходящи за semantic search / Q&A.

### Изисквания

- Python 3.10+
- Weaviate Cloud instance (URL + API key)
- Inference provider key (напр. OpenAI) — използва се от Agents

### Настройка на environment variables

Копирайте `.env.example` в `.env` и попълнете стойностите:

- **`WEAVIATE_URL`**
- **`WEAVIATE_API_KEY`**
- **`INFERENCE_API_KEY`**
- **`INFERENCE_PROVIDER`** (по подразбиране `openai`)

### Инсталация

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Зареждане на данни (schema + sample data)

```bash
python -m coursemind.setup_weaviate
```

### Стартиране на CLI асистента

```bash
python -m coursemind.cli
```

### Демонстрационни заявки (примерни 5+)

```bash
python -m coursemind.demo_queries
```

### Бележки

- Ключовете **не** се комитват. Ползвайте `.env`.
- Ако включите Transformation Agent, работете върху **test data** (модифицира обектите in-place).

