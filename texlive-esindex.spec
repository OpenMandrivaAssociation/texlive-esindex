Name:		texlive-esindex
Version:	52342
Release:	2
Summary:	Typset index entries in Spanish documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/esindex
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esindex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esindex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package helps you to create indexes in Spanish. With
esindex you can write, say, \esindex{canon} and the entry will
be correctly alphabetized in the index. This release of esindex
works with accented characters in any encoding, and without
babel.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/esindex
%doc %{_texmfdistdir}/doc/latex/esindex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
