#
# Conditional build:
%bcond_without	tests		# build without tests

Summary:	Run meld or any git difftool to interactively stage changes
Name:		git-meld-index
Version:	0.2.2
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	https://github.com/jjlee/git-meld-index/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fbb269be8d930fa412cc0cf2c154eef9
URL:		https://github.com/jjlee/git-meld-index
Requires:	git-core
Requires:	meld
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
git-meld-index runs meld, or any other git difftool (kdiff3, diffuse,
etc.) to allow you to interactively stage changes to the git index
(also known as the git staging area).

This is similar to the functionality of git add -p, and git add -i. In
some cases meld is easier / quicker to use than git add -p or the
staging feature in tools like git gui.

%prep
%setup -q

%build
%py_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/git-meld-index
%attr(755,root,root) %{_bindir}/git-meld-index-run-merge-tool
%{_mandir}/man1/git-meld-index.1*
%{py_sitescriptdir}/git_meld_index.py[co]
%{py_sitescriptdir}/git_meld_index-%{version}-py*.egg-info
