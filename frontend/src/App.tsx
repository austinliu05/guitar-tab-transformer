import { Routes, Route } from 'react-router-dom';
import CustomNavbar from './pages/Navbar';
import Home from './pages/Home';
import NotFound from './pages/NotFound';
import Footer from './components/Footer'
function App() {
  return (
    <div className="App">
      <CustomNavbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/home" element={<Home />} />
        <Route path="/binary-classification" />
        <Route path="/multiclass-classification" />
        <Route path="*" element={<NotFound />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
