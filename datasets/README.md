# Banking Datasets

This directory contains sample datasets for the Azure GenAI Banking Labs.

## Available Datasets

### 1. Banking Products (`banking/banking_products.csv`)
Contains information about various banking products and services.

**Columns:**
- `product_id`: Unique product identifier
- `product_name`: Product name
- `product_type`: Category (Savings Account, Credit Card, Loan, etc.)
- `description`: Detailed product description
- `interest_rate`: Annual interest rate (%)
- `minimum_balance`: Minimum balance requirement
- `monthly_fee`: Monthly maintenance fee
- `features`: Key product features

**Records:** 15 products

### 2. Transactions (`banking/transactions.csv`)
Sample banking transactions including normal and fraudulent activities.

**Columns:**
- `transaction_id`: Unique transaction identifier
- `account_id`: Account identifier
- `transaction_date`: Date and time of transaction
- `transaction_type`: Type (debit/credit)
- `amount`: Transaction amount
- `merchant`: Merchant name
- `category`: Transaction category
- `description`: Transaction description
- `fraud_flag`: Fraud indicator (0=normal, 1=fraudulent)

**Records:** 30 transactions (including 8 fraudulent)

### 3. Banking FAQ (`banking/banking_faq.csv`)
Frequently asked questions and answers for banking services.

**Columns:**
- `question_id`: Unique question identifier
- `category`: Question category
- `question`: Customer question
- `answer`: Detailed answer

**Records:** 20 FAQ entries

**Categories:**
- Account Opening
- Cards
- Loans
- Online Banking
- Transfers
- Fees
- Security
- Investments
- Mobile Banking
- Customer Service

## Usage

These datasets are used throughout the labs for:
- Testing Azure OpenAI chat completions
- Building RAG (Retrieval Augmented Generation) systems
- Training fraud detection models
- Creating semantic search applications
- Developing banking chatbots

## Data Privacy

⚠️ **Important:** All data in these datasets is synthetic and created for educational purposes only. Do not use real customer data in lab environments.

## License

These datasets are provided for educational use in the Azure GenAI Banking Course.

