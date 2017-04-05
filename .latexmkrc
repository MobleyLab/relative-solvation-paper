$pdf_mode = 1;
$dvi_mode = $postscript_mode = 0; 
$preview_mode = 0;
$pdf_previewer = 'evince %O %S';
@default_files = ('reprod.tex', 'SI.tex');

$pdflatex = 'internal _pdflatex %O %S';
sub _pdflatex{
  my @args = @_;
  system('make');  # a bit silly...
  return system('pdflatex', @args);
}

add_cus_dep('svg', 'pdf', 0, 'svg2pdf');
sub svg2pdf {
  return system("inkscape -z -A \"$_[0].pdf\" \"$_[0].svg\"")
}
