const Navbar = () => {
  return (
    <main className="bg-cyan-300 p-4">
      <div className="flex justify-between">
        <div className="flex">
          <div className="bg-red-400">VirgilBookStore</div>
          <div className="flex">
            <span className="px-4">Gênero</span>
            <span className="px-4">Autores</span>
          </div>
        </div>

        <div>
            <span>Login</span>
        </div>
      </div>
    </main>
  );
};

export default Navbar;
