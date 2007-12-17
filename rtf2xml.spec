%define version		1.33
%define release		1
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
%{py_platsitedir}/*

