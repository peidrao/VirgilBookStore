import { useEffect, useState } from "react";

import { usePathname } from "next/navigation";

const useNavigation = () => {
  const pathname = usePathname();

  const [isCategory, setIsCategory] = useState(false);
  const [isAuthor, setIsAuthor] = useState(false);
  const [isLogin, setIsLogin] = useState(false);

  useEffect(() => {
    setIsAuthor(false);
    setIsCategory(false);

    switch (pathname) {
      case "/categories":
        setIsCategory(true);
        break;
      case "/authors":
        setIsAuthor(true);
      case "/login":
        setIsLogin(true);
        break;
      default:
        break;
    }
  }, [pathname]);

  return {
    isCategory,
    isAuthor,
    isLogin,
  };
};

export default useNavigation;
