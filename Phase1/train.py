from datasets import load_dataset
from transformers import T5ForConditionalGeneration, AutoTokenizer, Trainer, TrainingArguments

MODEL_NAME = "t5-small"
OUTPUT_DIR = "./checkpoints"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)

# Load CNN/DailyMail dataset
raw = load_dataset("cnn_dailymail", "3.0.0")

# Preprocess function
def preprocess(batch):
    inputs = ["summarize: " + art for art in batch["article"]]
    model_inputs = tokenizer(
        inputs,
        max_length=1024,
        truncation=True,
        padding="max_length"
    )
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(
            batch["highlights"],
            max_length=150,
            truncation=True,
            padding="max_length"
        )
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

# Tokenize dataset
dataset = raw.map(
    preprocess,
    batched=True,
    remove_columns=["article", "highlights", "id"]
)

# Training arguments
training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    num_train_epochs=3,
    logging_steps=500,
    save_steps=1000,
    evaluation_strategy="steps",
    eval_steps=1000,
    save_total_limit=2,
)

# Trainer
def main():
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"],
        eval_dataset=dataset["validation"],
    )
    trainer.train()
    trainer.save_model(OUTPUT_DIR)

if __name__ == "__main__":
    main()