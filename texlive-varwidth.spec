Name:		texlive-varwidth
Version:	24104
Release:	1
Summary:	A variable-width minipage
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/varwidth
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/varwidth.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/varwidth.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The varwidth environment is superficially similar to minipage,
but the specified width is just a maximum value -- the box may
get a narrower "natural" width.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/varwidth/varwidth.sty
%doc %{_texmfdistdir}/doc/latex/varwidth/miscdoc.sty
%doc %{_texmfdistdir}/doc/latex/varwidth/varwidth-doc.pdf
%doc %{_texmfdistdir}/doc/latex/varwidth/varwidth-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
