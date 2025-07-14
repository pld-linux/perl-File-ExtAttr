#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	File
%define	pnam	ExtAttr
#
Summary:	File::ExtAttr - Perl extension for accessing extended attributes of files
Name:		perl-File-ExtAttr
Version:	1.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/R/RI/RICHDAWE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bcce46d86b72185f3814a7c413b86c8a
Patch0:		%{name}-xattr_path.patch
URL:		http://search.cpan.org/dist/File-ExtAttr/
BuildRequires:	attr-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::ExtAttr is a Perl module providing access to the extended
attributes of files. Extended attributes are metadata associated with
a file. Examples are access control lists (ACLs) and other security
parameters. But users can add their own key=value pairs.

Extended attributes may also not be supported by your filesystem or
require special options to be enabled for a particular filesystem.
E.g.:

mount -o user_xattr /dev/hda1 /some/path

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/File/ExtAttr.pm
%dir %{perl_vendorarch}/File/ExtAttr
%{perl_vendorarch}/File/ExtAttr/Tie.pm
%dir %{perl_vendorarch}/auto/File/ExtAttr
%attr(755,root,root) %{perl_vendorarch}/auto/File/ExtAttr/ExtAttr.so
%{perl_vendorarch}/auto/File/ExtAttr/autosplit.ix
%{_mandir}/man3/File::ExtAttr.3*
%{_mandir}/man3/File::ExtAttr::Tie.3*
