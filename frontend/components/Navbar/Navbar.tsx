"use client";

import useNavigation from "@/hook/use-navigation";

const Navbar = () => {
  const { isAuthor, isCategory, isLogin } = useNavigation();

  return (
    <main className="bg-slate-700">
      <div className="flex justify-between">
        <div className="flex">
          <div className="bg-red-400 p-4 text-white">
          VirgilBook<span className="uppercase font-bold">Store</span>

          </div>
          <div className="flex p-4 text-slate-400 justify-center uppercase font-semibold">
            <a className={isCategory ? "text-white" : "pr-4 hover:text-white"}>
              Categorias
            </a>
            <a className={isAuthor ? "text-white" : "pr-4 hover:text-white"}>
              Autores
            </a>
          </div>
        </div>

        <div className="flex items-center">
          <a
            href="/login"
            className={
              isLogin
                ? "p-4 uppercase font-semibold text-white"
                : "text-slate-400 p-4 uppercase font-semibold hover:text-white"
            }
          >
            Login
          </a>
        </div>
      </div>
    </main>
  );
};

export default Navbar;
