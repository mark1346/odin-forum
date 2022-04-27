import React from 'react';
import odinvision_logo from './odinvision_logo.svg';
import './styles.css';

const Logo = () => {
  return (
    <div className="logoContainer">
      <img src={odinvision_logo} className="logo" alt="logo" />
      <div className="logoTitle">Odin Forum</div>
    </div>
  );
};

export default Logo;
