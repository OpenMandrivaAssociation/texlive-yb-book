%global tl_name yb-book
%global tl_revision 79224

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.11.0
Release:	%{tl_revision}.1
Summary:	Template for YB Branded Books
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/yb-book
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yb-book.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yb-book.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yb-book.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(anyfontsize)
Requires:	texlive(biblatex)
Requires:	texlive(bigfoot)
Requires:	texlive(changepage)
Requires:	texlive(chngcntr)
Requires:	texlive(collection-fontsextra)
Requires:	texlive(collection-fontsrecommended)
Requires:	texlive(csquotes)
Requires:	texlive(cyrillic)
Requires:	texlive(doi)
Requires:	texlive(enumitem)
Requires:	texlive(fancyhdr)
Requires:	texlive(float)
Requires:	texlive(footmisc)
Requires:	texlive(geometry)
Requires:	texlive(href-ul)
Requires:	texlive(hypdoc)
Requires:	texlive(ifmtarg)
Requires:	texlive(imakeidx)
Requires:	texlive(lastpage)
Requires:	texlive(lh)
Requires:	texlive(libertine)
Requires:	texlive(mdframed)
Requires:	texlive(microtype)
Requires:	texlive(needspace)
Requires:	texlive(paralist)
Requires:	texlive(pgf)
Requires:	texlive(pgfopts)
Requires:	texlive(qrcode)
Requires:	texlive(setspace)
Requires:	texlive(soul)
Requires:	texlive(textpos)
Requires:	texlive(titlesec)
Requires:	texlive(ulem)
Requires:	texlive(wrapfig)
Requires:	texlive(xcolor)
Requires:	texlive(xifthen)
Requires:	texlive(xkeyval)
Requires:	texlive(zref)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This template helps the author design books published on Amazon under
the "Y.B." brand. You are welcome to use it too for your own books.

