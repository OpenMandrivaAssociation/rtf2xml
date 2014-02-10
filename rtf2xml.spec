Summary:		Converts RTF format to structured XML
Name:			rtf2xml
Version:		1.33
Release:		5
Source0:		http://belnet.dl.sourceforge.net/sourceforge/rtf2xml/rtf2xml-1.33.tar.bz2
URL:			http://rtf2xml.sourceforge.net/
License:		GPL
Group:			File tools
Requires:		python
BuildRequires:	python-devel
BuildArch:		noarch

%description
Converts a RTF file to structured XML.

%prep
%setup -q

%build
%{__python} setup.py build

%install
mkdir -p %{buildroot}%{_bindir}
%{__python} setup.py install --root=%{buildroot} --record rtf2xml.lst

%files
%doc README.txt
%attr(0755,root,root) %{_bindir}/*
%{py_puresitedir}/*
