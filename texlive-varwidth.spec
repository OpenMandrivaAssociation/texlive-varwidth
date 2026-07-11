%global tl_name varwidth
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.92
Release:	%{tl_revision}.1
Summary:	A variable-width minipage
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/varwidth
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/varwidth.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/varwidth.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The varwidth environment is superficially similar to minipage, but the
specified width is just a maximum value -- the box may get a narrower
"natural" width.

