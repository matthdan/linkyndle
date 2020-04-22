FROM python:3 as builder
WORKDIR /linkyndle
COPY . /linkyndle
RUN python setup.py sdist

FROM python:3 
WORKDIR /linkyndle
COPY --from=builder /linkyndle/dist/linkyndle-1.0.tar.gz .
RUN pip install linkyndle-1.0.tar.gz
CMD ["linkyndle", "--help"]