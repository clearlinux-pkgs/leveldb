#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : leveldb
Version  : 1.20
Release  : 5
URL      : https://github.com/google/leveldb/archive/v1.20.tar.gz
Source0  : https://github.com/google/leveldb/archive/v1.20.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: leveldb-lib
Patch1: 0112-makefile_install.patch

%description
This directory contains interfaces and implementations that isolate the
rest of the package from platform details.

%package dev
Summary: dev components for the leveldb package.
Group: Development
Requires: leveldb-lib
Provides: leveldb-devel

%description dev
dev components for the leveldb package.


%package lib
Summary: lib components for the leveldb package.
Group: Libraries

%description lib
lib components for the leveldb package.


%prep
%setup -q -n leveldb-1.20
%patch1 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1488465828
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1488465828
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/leveldb/c.h
/usr/include/leveldb/cache.h
/usr/include/leveldb/comparator.h
/usr/include/leveldb/db.h
/usr/include/leveldb/dumpfile.h
/usr/include/leveldb/env.h
/usr/include/leveldb/filter_policy.h
/usr/include/leveldb/iterator.h
/usr/include/leveldb/options.h
/usr/include/leveldb/slice.h
/usr/include/leveldb/status.h
/usr/include/leveldb/table.h
/usr/include/leveldb/table_builder.h
/usr/include/leveldb/write_batch.h
/usr/lib64/libleveldb.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libleveldb.so.1
/usr/lib64/libleveldb.so.1.20
