# 🌍 Global Language Detector

An end-to-end Natural Language Processing (NLP) solution that identifies the language of a given text using Machine Learning. Built with a focus on modularity and production-readiness.

## 🚀 Features
* **Automated Pipeline**: Uses Scikit-Learn `Pipeline` to bundle preprocessing and classification.
* **High Accuracy**: Achieves ~95.6% accuracy using a Multinomial Naive Bayes classifier.
* **Scalable Structure**: Separated training and inference scripts for easy deployment.
* **Multi-Language Support**: Capable of identifying diverse scripts including Tamil, Thai, Chinese, and Latin-based languages.

## 🛠️ Technical Stack
- **Language**: Python 3.x
- **Libraries**: `Pandas`, `NumPy`, `Scikit-Learn`
- **Algorithm**: Multinomial Naive Bayes (Ideal for text frequency data)
- **Feature Extraction**: Bag-of-Words via `CountVectorizer`

## 📦 Installation & Usage

1. **Clone and Install Dependencies**:
   ```bash
   pip install -r requirements.txt