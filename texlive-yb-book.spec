Name:		texlive-yb-book
Version:	70740
Release:	1
Summary:	Template for YB Branded Books
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/yb-book
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yb-book.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yb-book.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yb-book.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This template helps the author design books published on Amazon
under the "Y.B." brand. You are welcome to use it too for your
own books.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/yb-book
%{_texmfdistdir}/tex/latex/yb-book
%doc %{_texmfdistdir}/doc/latex/yb-book

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
