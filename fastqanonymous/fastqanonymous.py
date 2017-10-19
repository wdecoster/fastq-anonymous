from Bio import SeqIO
from argparse import ArgumentParser
from .version import __version__
import sys


def main():
    args = get_args()
    anonymize(args.fastq, args.mask)


def get_args():
    parser = ArgumentParser(description="Change the sequence of a fastq file \
                                        to enable sharing of confidential information, \
                                        for troubleshooting￼ of tools.")
    parser.add_argument("-v", "--version",
                        help="Print version and exit.",
                        action="version",
                        version='fastq-anonymous {}'.format(__version__))
    parser.add_argument("-m", "--mask",
                        help="Mask all nucleotides using N",
                        action="store_true")
    return parser.parse_args()


def anonymize(fastq, masking):
    for rec in SeqIO.parse(sys.stdin, "fastq"):
