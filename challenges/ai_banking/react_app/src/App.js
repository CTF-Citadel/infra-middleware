import './App.css';
import { Route, Routes } from "react-router-dom";
import NavBar from './navBar';
import Home from './subpages/home';
import Footer from './footer';
import TOS from './rndm_pages/tos';
import PP from './rndm_pages/pp';
import FAQ from './rndm_pages/faq';
import C from './rndm_pages/c';
import PR from './rndm_pages/pr';
import IR from './rndm_pages/ir';
import Login from './subpages/login';
import Signup from './subpages/signup';
import Profile from './subpages/profile';

function App() {
  return (
    <div className="App">
      <NavBar />
      <Routes>
        <Route exact path="/" element={<Home/>} />
        <Route exact path="/terms" element={<TOS/>} />
        <Route exact path="/privacy" element={<PP/>} />
        <Route exact path="/faq" element={<FAQ/>} />
        <Route exact path="/careers" element={<C/>} />
        <Route exact path="/press" element={<PR/>} />
        <Route exact path="/investor" element={<IR/>} />
        <Route exact path="/login" element={<Login/>} />
        <Route exact path="/signup" element={<Signup/>} />
        <Route exact path="/profile" element={<Profile/>} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
