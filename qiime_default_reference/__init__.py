import hashlib
import os.path

__version__ = "0.1.0"

def get_reference_sequences():
    """Return absolute filepath to default reference sequences.

    Current default is Greengenes 13_8 97% OTU representative sequences.

    """
    return _get_reference_data('gg_13_8_otus', 'rep_set', '97_otus.fasta')


def get_reference_taxonomy():
    """Return absolute filepath to default reference taxonomy.

    Current default is Greengenes 13_8 97% OTU representative sequence taxonomic
    assignments.

    """
    return _get_reference_data(
        'gg_13_8_otus', 'taxonomy', '97_otu_taxonomy.txt')


def get_template_alignment():
    """Return absolute filepath to default template alignment.

    Current default is Greengenes 13_8 85% OTU aligned representative sequences.

    """
    return _get_reference_data(
        'gg_13_8_otus', 'rep_set_aligned', '85_otus.fasta')


def get_template_alignment_column_mask():
    """Return 16S alignment Lane mask as a string.

    Lane mask is derived from:
        Lane,D.J. (1991) 16S/23S rRNA sequencing. In Stackebrandt,E. and
        Goodfellow,M. (eds), Nucleic Acid Techniques in Bacterial Systematics.
        John Wiley and Sons, New York, pp. 115-175.

    Lane mask was originally available in ARB. For more information on ARB, see:
        http://www.ncbi.nlm.nih.gov/pubmed/14985472

    16S alignment Lane mask taken from:
        http://greengenes.lbl.gov/Download/Sequence_Data/lanemask_in_1s_and_0s

    The trailing newline that is present in the original file has been removed.

    """
    return '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000110111101011001110100101101011001000010100111111010110101110111010111000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011010110101101001000000000000011101111101001101101010101100011100101101001010111001101000000000000000000000000000000000000000000000000000000000000000000101100001110110110111000000000000000000000000010101000000000000000000000001110100011101110111101100011010010110100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100001010001011010001100010100000101110111001011100100000011001001011010000100011110101011010100001110110101010111100101101010010110100000000000011101010000001101101010111010110000100110110010110101101111010111110010101101011010110101011111101111011101001010101011010110101011000110101011101111101011010110011011010000101011010110110110111101111010110100010101001001101010010010101011000001101100000000010101010101001000110101110000000011011010100101110000110100100000000000000000000000000000000000000000000000000000000000000000001101101010110101101000000000110000000000011111011101101011100010110111100111100101000100111100010110011011001100011011011101110101011011110101110110110100101001111011100001101111011001011010101010000000000001001011010101011000010101010001011101101011011001101110100000000000000000000000000000000000000000000000000000000000000000000110101100000000000000000000000000000000000000000000000000000000000000000000000001101010110110100001010101010100000000100110101010101011100101010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001010101010101000001011001101010000000000001011010110100001100111101110101100110101110111111011011101111010110101110011010110101101100100100110111010010100010000100101011111000000101101100000000000000000000000000000000000000000000000000000000000000110101010011001100000110110110010101110011010100000000000000101111011101010111100110111101011101000001101010111010100001011001010111010111001011110110011011000000000101100100101011010100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000101010101101000000110010000110111001101010100100110110010000101110111010101101110110001110000010100101010101110100111011110111000000000111101110111110101011110000101001010101110110100100110110100110111011011110101011101111010110101101010110110101101111101101011010101000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001010101010111101101110110011101110101101100010110110100111011011101011010110110110111110110000000010111011101011101010110011001011110010101010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000101001100000000000000010101010101101001101010111001010000000000000000000000000000000000001010001110000000000000000000000000000000000101010100101011010011101001111010111101110011110100011101010101010101110000110100110101011011011011101111101001100111110001011110101001011101101100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000101010101001011110100100000000000000000000000000000000000000010110101000000000001001010110001000000000010011101000000101011111011010101010111011100000000111010111110110010111101101000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010111110101010110101101111101101011001011011010101000011101101010100000001100111011010110101110111101011111111101111000011111110111011100000100011001110110110100100011101011011011100101110000001001011100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000111001100111010000101110110111000000000000000000000000110011101111011011101111111110111110111100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'


# Copied and modified from
# https://github.com/biocore/scikit-bio/blob/master/skbio/util/_misc.py
# See licenses/scikit-bio.txt for more details.
def safe_md5(open_file, block_size=2 ** 20):
    """Computes an md5 sum without loading the file into memory

    Parameters
    ----------
    open_file : file object
        open file handle to the archive to compute the checksum. It
        must be open as a binary file
    block_size : int, optional
        size of the block taken per iteration

    Returns
    -------
    md5 : md5 object from the hashlib module
        object with the loaded file

    Notes
    -----
    This method is based on the answers given in:
    http://stackoverflow.com/a/1131255/379593

    Examples
    --------
    >>> from StringIO import StringIO
    >>> from qiime_default_reference import safe_md5
    >>> fd = StringIO("foo bar baz") # open file like object
    >>> x = safe_md5(fd)
    >>> x.hexdigest()
    'ab07acbb1e496801937adfa772424bf7'
    >>> fd.close()

    """
    md5 = hashlib.md5()
    data = True
    while data:
        data = open_file.read(block_size)
        if data:
            md5.update(data)
    return md5


def _get_reference_data(*args):
    fp = os.path.join(_get_package_dir(), *args)

    if not os.path.exists(fp):
        raise IOError(
            "Reference data file %s is missing from installation." % fp)
    return fp


# Copied and modified from qiime.util.get_qiime_project_dir:
# https://github.com/biocore/qiime/blob/master/qiime/util.py
# The author of the function (Greg Caporaso) gave permission to use his GPL
# code in this project without requiring that this project also become GPL.
def _get_package_dir():
    return os.path.dirname(os.path.abspath(__file__))
