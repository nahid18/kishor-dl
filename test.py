import unittest
from kishor import get_pdf_list

class TestKishor(unittest.TestCase):

  def test_pdf(self):
    result = get_pdf_list(['https://wp.me/p4gPEb-47z'])
    expection = [{'title': 'জানুয়ারী-২০২০', 'pdfUrl':'http://www.kishorkanthabd.com/wp-content/uploads/2020/06/kk-Janu20-With-cover-Photo_ok.pdf'}]
    self.assertEqual(result, expection)


if __name__ == '__main__':
  unittest.main()

