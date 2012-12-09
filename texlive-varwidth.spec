# revision 24104
# category Package
# catalog-ctan /macros/latex/contrib/varwidth
# catalog-date 2010-11-26 12:00:18 +0100
# catalog-license lppl
# catalog-version 0.92
Name:		texlive-varwidth
Version:	0.92
Release:	2
Summary:	A variable-width minipage
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/varwidth
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/varwidth.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/varwidth.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.92-2
+ Revision: 757407
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.92-1
+ Revision: 719875
- texlive-varwidth
- texlive-varwidth
- texlive-varwidth

