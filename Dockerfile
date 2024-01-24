FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
RUN pip install -e .

EXPOSE 8501

CMD ["streamlit", "run", "meeting_cost_calculator/frontend.py", "--server.port", "8501"]
