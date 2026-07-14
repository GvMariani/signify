Summary:		Sign and verify signatures on files
Name:	signify
Version:		33
Release:		1
License:	ISC
Group:	Security
Url:	https://codeberg.org/aperezdc/signify
Source0:	https://github.com/aperezdc/signify/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:		make
BuildRequires:		pkgconfig(libbsd) >= 0.11.0
BuildRequires:		pkgconfig(libmd)

%description
This utility creates and verifies cryptographic signatures, as used by the
OpenBSD release maintainers.

%files
%license COPYING
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
# No configure: only makefile
%set_build_flags
%make_build LTO=1


%install
%make_install PREFIX=%{_prefix}


%check
make check
