import { Routes, Route } from 'react-router-dom';
import CustomNavbar from './components/Navbar';
import Home from './pages/Home';
import NoteheadBlog from './pages/NoteheadBlog';
import NotFound from './pages/NotFound';
import Footer from './components/Footer'
import TeamPage from './pages/TeamPage';

function App() {
  return (
    <div className="App">
      <CustomNavbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/home" element={<Home />} />
        <Route 
          path="/blog/notehead-classification" 
          element={<NoteheadBlog/>} 
        />
          <Route 
          path="/team" 
          element={<TeamPage/>} 
        />
        <Route path="*" element={<NotFound />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
