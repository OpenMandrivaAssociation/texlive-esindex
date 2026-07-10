%global tl_name esindex
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.8
Release:	%{tl_revision}.1
Summary:	Generate sorting keys for indexes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/esindex
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esindex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esindex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
With this package sorting keys can be automatically generated. It was
originally devised for Spanish, so that, say, \esindex{canon} is
correctly alphabetized in the index, but it can be configured to
generate sorting keys for other languages, with custom replacements and
multilevel comparisons.

