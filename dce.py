import React, {Component} from 'react';
import './css/bootstrap.min.css';
class Header extends Component {
    render() {
        return (
            <header className="masthead bg-primary text-white text-center" color='background-color: #0d0d0e!important;'>
                <div className="container d-flex align-items-center flex-column">
                    <img className="masthead-avatar mb-5" src="assets/img/avataaars.svg" alt="" />
                    {/* Masthead Heading*/}
                  
                    {/* Icon Divider*/}
                    <div className="divider-custom divider-light">
                        <div className="divider-custom-line" />
                        <div className="divider-custom-icon"><i className="fas fa-star" /></div>
                        <div className="divider-custom-line" />
                    </div>
                    {/* Masthead Subheading*/}
                    <p className="masthead-subheading font-weight-light mb-0">content</p>
                </div>
 <div className="container d-flex align-items-center flex-column">
                    <img className="masthead-avatar mb-5" src="assets/img/avataaars.svg" >
                    {/* Masthead Heading*/}

                    {/* Icon Divider*/}
                    <div className="divider-custom divider-light">
                        <div className="divider-custom-line" />
                        <div className="divider-custom-icon"><i className="fas fa-star" />
                        <div className="divider-custom-line" />
                    </div>
                    {/* Masthead Subheading*/}
                    <p className="masthead-subheading font-weight-light mb-0">content</p>
                </div>
            </header>
        );
    }
}

export default Header;
