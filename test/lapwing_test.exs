defmodule LapwingTest do
  use ExUnit.Case
  doctest Lapwing

  test "greets the world" do
    assert Lapwing.hello() == :world
  end
end
