$recorder = 1;
$pdf_mode = 1;
$bibtex_use = 2;
$clean_ext .= 'acs-%R.bib lod';
$dvi_mode = $postscript_mode = 0; 
$preview_mode = 0;
$pdf_previewer = 'evince %O %S';
@default_files = ('SI.tex', 'reprod.tex');

$pdflatex = 'make && pdflatex %O %S';

add_cus_dep('svg', 'pdf', 0, 'svg2pdf');
sub svg2pdf {
  return system("inkscape -z -A \"$_[0].pdf\" \"$_[0].svg\"")
}
