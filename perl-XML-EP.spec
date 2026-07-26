%define upstream_name 	 XML-EP
Name:		perl-%{upstream_name}
Version:	0.01
Release:	6

Summary:	%{upstream_name} perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/XML-EP
Source0:	https://cpan.metacpan.org/authors/id/J/JW/JWIED/XML-EP-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
Requires:	perl(XML::Parser)
Requires:	perl(XML::XSLT)
BuildArch:	noarch

%description
%{upstream_name} attempts to follow the Cocoon ideas and principles, 
but in a Perl environment.

%prep
%setup -q  -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%install
%makeinstall_std

%files 
%doc ChangeLog README MANIFEST examples
%{_bindir}/*
%{perl_vendorlib}/XML/*.pm
%{perl_vendorlib}/XML/EP/*
%{_mandir}/*/*

%changelog
* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.0
+ Revision: 401865
- rebuild using %0.01 Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.01-12mdv2009.0
+ Revision: 242200
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.01-10mdv2008.0
+ Revision: 23516
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.01-9mdk
- Fix According to perl Policy
	- Source URL
	- URL
- use mkrel

* Thu Sep 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.01-8mdk
- rebuild

* Thu Aug 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.01-7mdk
- rebuild for new perl
- drop $RPM_OPT_FLAGS, noarch..
- use %%makeinstall_std macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.01-6mdk
- rebuild for new auto{prov,req}

