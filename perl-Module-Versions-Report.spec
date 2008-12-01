#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Module
%define		pnam	Versions-Report
Summary:	Module::Versions::Report - report versions of all modules in memory
Summary(pl.UTF-8):	Module::Versions::Report - raportowanie wersji wszystkich modułów w pamięci
Name:		perl-Module-Versions-Report
Version:	1.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9c7efaa4c3dd8eecceb8e5d17476479b
URL:		http://search.cpan.org/dist/Module-Versions-Report/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
I often get email from someone reporting a bug in a module I've written.
I email back, asking what version of the module it is, what version of
Perl on what OS, and sometimes what version of some relevant third library
(like XML::Parser). They reply, saying "Perl 5". I say "I need the exact
version, as reported by `perl -v`". They tell me. And I say "I, uh,
also asked about the version of my module and XML::Parser [or whatever]".
They say "Oh yeah. It's 2.27". "Is that my module or XML::Parser?"
"XML::Parser." "OK, and what about my module's version?" "Ohyeah.
That's 3.11." By this time, days have passed, and what should have been
a simple operation - reporting the version of Perl and relevant modules,
has been needlessly complicated.

This module is for simplifying that task. If you add "use
Module::Versions::Report;" to a program (especially handy if your program
is one that demonstrates a bug in some module), then when the program
has finished running, you well get a report detailing the all modules
in memory, and noting the version of each (for modules that defined a
$VERSION, at least).

%description -l pl.UTF-8
Autor często dostaje raporty błędów w napisanych przez niego modułów.
Odpisując pyta się o wersję modułu, wersję Perla, system operacyjny i
czasem wersje powiązanych bibliotek (np. XML::Parser). W odpowiedzi
często dostaje "Perl 5", podczas gdy potrzebuje dokładnej wersji,
takiej jak wypisywana przez `perl -v`". I podobnie dla innych modułów.
Całą ta konwersacja może trwać wiele dni, a powinna być prostą
operacją - raportowaniem wersji Perla i powiązanych modułów.

Ten moduł służy do uproszczenia tego zadania. Po dodaniu "use
Module::Versions::Report" do programu (co jest szczególnie poręczne,
jeśli program służy do demonstrowania błędu w module), program po
uruchomieniu wypisuje raport ze szczegółami na temat wszystkich
modułów obecnych w pamięci, podając ich wersje (przynajmniej dla
modułów definiujących $VERSION).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%dir %{perl_vendorlib}/Module/Versions
%{perl_vendorlib}/Module/Versions/*.pm
%{_mandir}/man3/*
