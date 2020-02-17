import packer.rectangle as r
import packer.slicedLine as sl

# Measures number of items can fit inside the container which is rectangle.
# Longer dimension is width
class Measurer:
    def __init__(
        self, containerSurface: r.Rectangle, itemSurface: r.Rectangle, minSpace: int
    ):
        self.container = containerSurface
        self.item = itemSurface
        self.minSpace = minSpace

    # Finds the number of items can fit in width of the container
    def numberFitWCustom(
        self, container: r.Rectangle, item: r.Rectangle, minSpace: int
    ) -> sl.SlicedLine:
        # First cut the container width from one side (considered left side)
        cuttedWidth = container.width - minSpace
        # Number of items can fit inside the container horizontally
        count = cuttedWidth // (item.width + minSpace)
        if count < 0:
            return sl.SlicedLine(container.width, 0)
        # Return the width with maximum number of items
        # space + count * itemWidthIncludingOneSideSpace
        return sl.SlicedLine(1 + count * (item.width + 1), count)

    # Finds the number of items can fit in width of the container
    def numberFitW(self) -> sl.SlicedLine:
        return self.numberFitWCustom(self.container, self.item, self.minSpace)

    # Finds the number of items can fit in height of the container
    def numberFitHCustom(
        self, container: r.Rectangle, item: r.Rectangle, minSpace: int
    ) -> sl.SlicedLine:
        # First cut the container width from one side (considered left side)
        cuttedHeight = container.height - minSpace
        # Number of items can fit inside the container vertically
        count = cuttedHeight // (item.height + minSpace)
        if count < 0:
            return sl.SlicedLine(container.height, 0)
        # Return the height with maximum number of items
        # space + count * itemHeightIncludingOneSideSpace
        return sl.SlicedLine(1 + count * (item.height + 1), count)

    # Finds the number of items can fit in height of the container
    def numberFitH(self) -> sl.SlicedLine:
        return self.numberFitHCustom(self.container, self.item, self.minSpace)

    # Measures number of items inside the container
    def Measure(self) -> int:
        # Horizontal
        SlicedLineW = self.numberFitW()
        # Extra space remaining after placing items horizontally
        # Note we include space to the width of the item
        extraSpaceW = self.container.width - SlicedLineW.length
        # Vertical
        SlicedLineH = self.numberFitH()
        # Extra space remaining after placing items vertically
        # Note we include space to the height of the item
        extraSpaceH = self.container.height - SlicedLineH.length

        # So far, so good...
        # We found 2 new areas.
        # One = certainly items fit inside perfectly
        # Two = an area possible to place some more items inside it
        certainCount = SlicedLineW.count * SlicedLineH.count
        # Number of items which can be placed inside the extra space
        moreItemsCount = self.MeasureExtraArea(extraSpaceW, extraSpaceH)

        return certainCount + moreItemsCount

    # Measures number of items inside the extra space of container
    def MeasureExtraArea(self, extraSpaceW: int, extraSpaceH: int) -> int:
        container = r.Rectangle(extraSpaceW, extraSpaceH)
        # Horizontal
        SlicedLineW = self.numberFitWCustom(container, self.item, self.minSpace)
        # Vertical
        SlicedLineH = self.numberFitHCustom(container, self.item, self.minSpace)
        return SlicedLineW.count * SlicedLineH.count

