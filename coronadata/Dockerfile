FROM python:3


LABEL FILE="ISRAEL COVID STATS"

RUN pip install requests
RUN pip install argparse

COPY ./coronafile.py ./

CMD ["python3", "coronafile.py", "-c", "israel"]
