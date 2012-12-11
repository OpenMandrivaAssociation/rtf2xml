%define version		1.33
%define release		4
%define name		rtf2xml

Summary:		Converts RTF format to structured XML
Name:			%{name}
Version:		%{version}
Release:		%mkrel %{release}
Source0:		http://belnet.dl.sourceforge.net/sourceforge/rtf2xml/rtf2xml-1.33.tar.bz2
URL:			http://rtf2xml.sourceforge.net/
License:		GPL
Group:			File tools
Requires:		python
BuildRequires:		python-devel
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root

%description
Converts a RTF file to structured XML.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
%{__python} setup.py install --root=%{buildroot} --record rtf2xml.lst

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.txt
%attr(0755,root,root) %{_bindir}/*
%{py_puresitedir}/*



%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.33-4mdv2010.0
+ Revision: 442767
- rebuild

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 1.33-3mdv2009.1
+ Revision: 326015
- rebuild

* Mon Dec 17 2007 Giuseppe Ghibò <ghibo@mandriva.com> 1.33-2mdv2008.1
+ Revision: 121644
- Rebuilt.
- Use %%py_puresitedir in %%files.
- Add python-devel to BuildRequires.
- Added python to buildrequires.
- Initial release.
- import rtf2xml


