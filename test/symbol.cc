#include <napi.h>

using namespace Napi;

Symbol CreateNewSymbolWithNoArgs(const Napi::CallbackInfo& info) {
  (void)info;
  return Napi::Symbol();
}

Symbol CreateNewSymbolWithCppStrDesc(const Napi::CallbackInfo& info) {
  String cppStrKey = info[0].As<String>();
  return Napi::Symbol::New(info.Env(), cppStrKey.Utf8Value());
}

Symbol CreateNewSymbolWithCStrDesc(const Napi::CallbackInfo& info) {
  String cStrKey = info[0].As<String>();
  return Napi::Symbol::New(info.Env(), cStrKey.Utf8Value().c_str());
}

Symbol CreateNewSymbolWithNapiString(const Napi::CallbackInfo& info) {
  String strKey = info[0].As<String>();
  return Napi::Symbol::New(info.Env(), strKey);
}

Symbol GetWellknownSymbol(const Napi::CallbackInfo& info) {
  String registrySymbol = info[0].As<String>();
  return Napi::Symbol::WellKnown(info.Env(),
                                 registrySymbol.Utf8Value().c_str());
}

Symbol FetchSymbolFromGlobalRegistry(const Napi::CallbackInfo& info) {
  String registrySymbol = info[0].As<String>();
  return Napi::Symbol::For(info.Env(), registrySymbol.Utf8Value().c_str());
}

Object InitSymbol(Env env) {
  Object exports = Object::New(env);

  exports["createNewSymbolWithNoArgs"] =
      Function::New(env, CreateNewSymbolWithNoArgs);
  exports["createNewSymbolWithCppStr"] =
      Function::New(env, CreateNewSymbolWithCppStrDesc);
  exports["createNewSymbolWithCStr"] =
      Function::New(env, CreateNewSymbolWithCStrDesc);
  exports["createNewSymbolWithNapi"] =
      Function::New(env, CreateNewSymbolWithNapiString);
  exports["getWellKnownSymbol"] = Function::New(env, GetWellknownSymbol);
  exports["getSymbolFromGlobalRegistry"] =
      Function::New(env, FetchSymbolFromGlobalRegistry);
  return exports;
}
