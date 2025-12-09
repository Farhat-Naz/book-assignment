import React from 'react';
import NavbarContent from '@theme-original/Navbar/Content';
import UserDropdown from '@site/src/components/Auth/UserDropdown';
import type {WrapperProps} from '@docusaurus/types';
import type NavbarContentType from '@theme/Navbar/Content';

type Props = WrapperProps<typeof NavbarContentType>;

export default function NavbarContentWrapper(props: Props): JSX.Element {
  return (
    <>
      <NavbarContent {...props} />
      <UserDropdown />
    </>
  );
}
